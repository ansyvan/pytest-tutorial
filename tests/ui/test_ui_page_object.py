from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    
    sign_in_page = SignInPage() # create page object
    sign_in_page.go_to()    # open page https://github.com/login

    sign_in_page.try_login("page_object@gmail.com", "wrong password")  # try to login GitHub

    # check if the page name is the one we expect
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()    # close browser