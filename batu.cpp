#include <cstdlib>
#include <string>
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
    if (argc!=2)
        return Error("Invalid number of arguments");
    
    auto path = std::string(argv[1]);
    if (!std::filesystem::exists(path))
        return Error("File does not exist");

    system(("python src\\main.py "+path).c_str());
}