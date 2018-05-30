from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os

class LibgpgerrorConan(ConanFile):
    name = "libgpg-error"
    version = "1.31"
    license = "GPL-2.0"
    url = "https://github.com/weatherhead99/conan-libgpg-error/"
    description = "Libgpg-error is a small library that defines common error values for all GnuPG components."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"

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

