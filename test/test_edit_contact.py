from model.contact import Contact


def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Sarah")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", lastname="Connor"))
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)