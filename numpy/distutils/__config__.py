# This file is generated by C:\Minonda\conda-bld\work\numpy-1.11.1\setup.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

mkl_info={'include_dirs': ['C:\\Minonda\\envs\\_build\\Library\\include'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'libraries': ['mkl_core_dll', 'mkl_intel_lp64_dll', 'mkl_intel_thread_dll'], 'library_dirs': ['C:\\Minonda\\envs\\_build\\Library\\lib']}
blas_mkl_info={'include_dirs': ['C:\\Minonda\\envs\\_build\\Library\\include'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'libraries': ['mkl_core_dll', 'mkl_intel_lp64_dll', 'mkl_intel_thread_dll'], 'library_dirs': ['C:\\Minonda\\envs\\_build\\Library\\lib']}
openblas_lapack_info={}
blas_opt_info={'include_dirs': ['C:\\Minonda\\envs\\_build\\Library\\include'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'libraries': ['mkl_core_dll', 'mkl_intel_lp64_dll', 'mkl_intel_thread_dll'], 'library_dirs': ['C:\\Minonda\\envs\\_build\\Library\\lib']}
lapack_opt_info={'include_dirs': ['C:\\Minonda\\envs\\_build\\Library\\include'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'libraries': ['mkl_lapack95_lp64', 'mkl_core_dll', 'mkl_intel_lp64_dll', 'mkl_intel_thread_dll'], 'library_dirs': ['C:\\Minonda\\envs\\_build\\Library\\lib']}
lapack_mkl_info={'include_dirs': ['C:\\Minonda\\envs\\_build\\Library\\include'], 'define_macros': [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)], 'libraries': ['mkl_lapack95_lp64', 'mkl_core_dll', 'mkl_intel_lp64_dll', 'mkl_intel_thread_dll'], 'library_dirs': ['C:\\Minonda\\envs\\_build\\Library\\lib']}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    