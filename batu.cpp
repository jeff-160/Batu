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

    std::string ext = ".batu";
    if (path.find(ext)!=path.length()-ext.length())
        return Error("File format not supported");

    system(("python src\\main.py "+path).c_str());
}