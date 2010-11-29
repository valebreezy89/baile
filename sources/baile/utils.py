def create_instance(name, args=dict()):
    '''create new class instance for name
    Name should be fully-qualified class name
    '''
    parts = name.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)            
    return m(**args)