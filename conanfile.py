from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os

class LibgpgerrorConan(ConanFile):
    name = "libgpg-error"
    version = "1.31"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Libgpgerror here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        tools.get("https://www.gnupg.org/ftp/gcrypt/libgpg-error/%s-%s.tar.bz2" 
                  % (self.name, self.version))
        

    def build(self):
        abe = AutoToolsBuildEnvironment(self)
        source_sub = os.path.join(self.source_folder,
                                  "%s-%s" % (self.name,self.version))
        
        
        libfolder = os.path.join(self.package_folder,"lib")
        config_args = ["--libdir=%s" % libfolder, "--disable-languages",
                       "--disable-doc"]
        if self.options.shared:
            config_args.extend(["--enable-static=no", "--enable-shared=yes"])
        else:
            config_args.extend(["--enable-static=yes", "--enable-shared=no"])
            
        abe.configure(configure_dir=source_sub, args=config_args)
        abe.make()
        abe.make(target="check")
        abe.make(target="install")
        
    def package(self):
        pass
    
    def package_info(self):
        self.cpp_info.libs = ["gpg-error"]

