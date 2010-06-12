from utils.testing import slow, online, notimplemented, set_testing_pythonpath, acceptance
from utils.cache import TimedCache

def setup_module():
    # Note this is defined in models.__init__.py for real operation
#    print "============>Setting database name to MEMORY"
#    MODELS_DB = 'sqlite:///:memory:'
    set_testing_pythonpath()
#    setup_test_database()
    TimedCache().collect()
    #TimedCache().clear_cache()

def teardown_module():
    TimedCache().store_cache()
    print TimedCache().print_hits_and_misses()

def setup_test_database():
#    print "============>Creating a new database"
#    from sqlalchemy import create_engine, MetaData
#    from sqlalchemy.orm import sessionmaker, scoped_session
#    engine = create_engine(MODELS_DB, echo=True)
#    metadata = MetaData(engine)
#    Session = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=True))

	#import os
	#from models import DB_NAME
	#print "Deleting the database!"
	#os.system("rm " + DB_NAME)
	pass

#def setup_module():
#    #TimedCache().is_bypass_cache(True)    
#    print TimedCache()._caches.keys()    
#    pass
    
#def teardown_module():
#    TimedCache().is_bypass_cache(False)
#    TimedCache().print_hits_and_misses() 
#    TimedCache().store_cache() 
#    print TimedCache()._caches.keys()
