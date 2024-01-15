#include <cstdlib>
#include <string>
#include <windows.h>
#include <filesystem>

int Error(char* message){
    system(
        ("powershell -command Write-Host "+
        std::string(message)+
        std::string(" -ForegroundColor 'red'")).c_str()
    );
    return 0;
}

int main(int argc, char* argv[]){
    switch (argc){
        case 1:
            puts("Usage: batu [.batu sourcefile]");
        break;
        
        case 2:
            {
                auto path = std::string(argv[1]);
                if (!std::filesystem::exists(path))
                    return Error("File does not exist");

                std::string ext = ".batu";
                if (path.find(ext)!=path.length()-ext.length())
                    return Error("File format not supported");

                char buffer[MAX_PATH];
                GetModuleFileName(NULL, buffer, MAX_PATH);
                system((std::filesystem::path(buffer).parent_path().string()+"\\src\\main.exe "+path).c_str());
            }
        break;

        default:
            return Error("Invalid number of arguments");
    }   
}