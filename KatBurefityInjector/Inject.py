def Inject(process_name : str, dll_path : str):
    from pymem import Pymem
    import pymem.process as process

    converted_utf8 = bytes(dll_path, "utf-8")
    process_x = Pymem("{}.exe".format(process_name))
    handleproc = process_x.process_handle
    process.inject_dll_from_path(handleproc, converted_utf8)