import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contacts(app):
    app.session.login(user_name='exjfizhh@firste.ml', password='admin')
    app.contact.fill_required_fields(Contact(first_name='Alexsandr', last_name='Ivanov',
                                          adress='Moscow, Lenina streer, house 8', city='Moscow', post_code=152121,
                                          value_of_country='176', zone_in_country='2761'))
    app.session.exit_from_profile()