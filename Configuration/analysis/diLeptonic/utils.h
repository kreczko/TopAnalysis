#ifndef util_h
#define util_h

#include "classes.h"
#include <map>
#include <TString.h>
#include <TFile.h>
#include <TStyle.h>
#include <iostream>
#include <type_traits>
#include <cstdlib>
 
//convert LorentzVector to an array[E, px, py, pz]
void LVtod4(const LV lv, double *d);

// convert double to string (smart number of digits)
std::string d2s(double d);

void setHHStyle(TStyle& HHStyle);


////////////////////

class RootFileReader {
    std::map<TString, TFile*> fileMap;
    std::vector<TString> fileOrder;
    std::map<TString, int> accessed, opened;
    
    TObject* GetObj(const char* filename, const char* histoname, bool allowNonexisting);
    RootFileReader() {};
    ~RootFileReader();
public:
    //returns the singleton instnce
    static RootFileReader* getInstance();
    
    //need to put code for templated functions in the header file to allow compilation
    
    //get a histogram from the file
    template <typename T>
    void Get(const char* filename, const char* histoname, T& result, bool allowNonexisting = false) {
        //is_assignable seems to be missing in this gcc version
        //static_assert(std::is_assignable<TObject*, T>::value == true, "You must convert to a TObject* like type!");
        static_assert(std::is_pointer<T>::value == true, "You must convert to a TObject* like type!");
        TObject *obj = GetObj(filename, histoname, allowNonexisting);
        if (obj == nullptr) {
            if (allowNonexisting) {
                std::cerr << "Warning: " << histoname << " is not in " << filename << std::endl;
                result = nullptr;
                return;
            } else {
                std::cerr << "ERROR: " << histoname << " is not in " << filename << std::endl;
                std::exit(1);
            }            
        }
        result = dynamic_cast<T>(obj);
        if (!result) {
            std::cerr << "The histogram " << histoname << " in file " << filename 
                << " is of incompatible type (cannot typecast)!" << std::endl;
            std::exit(1);
        }
    }

    //get a histogram from the file, you need to pass the type here
    //warning: histo will be deleted once 60 more files have been opened
    template <typename T>
    const T* Get(const char* filename, const char* histoname, bool allowNonexisting = false) {
        T* result;
        Get(filename, histoname, result, allowNonexisting);
        return result;
    }
    
    template <typename T>
    T* GetClone(const char* filename, const char* histoname, bool allowNonexisting = false) {
        T* result;
        Get(filename, histoname, result, allowNonexisting);
        return static_cast<T*>(result->Clone());
    }
};

#endif