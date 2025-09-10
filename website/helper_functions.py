'''
helper_functions.py - audrey palmer

functions intended to be used in blueprint_pages.py and functional_pages.py but
stored here for the sake of organization
'''

from .database import db
from .models import User, Page, Visit


# functions -----------------------------------------------------------------------
def defining_absent_page(page_name) :
    ''' if a page hasnt been defined within the database for some reason, creates
        a new entry for it for the sake of metrics later! '''
    
    page = Page.query.filter_by(page_name = page_name).first()

    if page is None :

        new_page = Page(page_name = page_name)
        db.session.add(new_page)
        db.session.commit()

        return new_page
    
    return page


def increment_page_views(page) :
    ''' add 1 to the page view counter '''

    page.views += 1
    db.session.commit()