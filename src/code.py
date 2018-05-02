import amber
import seas
import personal_docks
import ships
import datetime
# import seanui
import frontend

if __name__ == "__main__":
    boula = personal_docks.PersonalDock.RegisterAccount(name="Boula", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    plasma_sea = seas.Sea.RegisterSea(creator=boula, name="Plasma Sea", description="I couldn't help but\nwhat?")
    a = personal_docks.PersonalDock.RegisterAccount(name="a", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    b = personal_docks.PersonalDock.RegisterAccount(name="b", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    c = personal_docks.PersonalDock.RegisterAccount(name="c", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    d = personal_docks.PersonalDock.RegisterAccount(name="d", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    e = personal_docks.PersonalDock.RegisterAccount(name="e", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    f = personal_docks.PersonalDock.RegisterAccount(name="f", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    g = personal_docks.PersonalDock.RegisterAccount(name="g", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    h = personal_docks.PersonalDock.RegisterAccount(name="h", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    i = personal_docks.PersonalDock.RegisterAccount(name="i", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    amber.database[boula].join_sea(plasma_sea)
    amber.database[a].join_sea(plasma_sea)
    amber.database[b].join_sea(plasma_sea)
    amber.database[c].join_sea(plasma_sea)
    amber.database[d].join_sea(plasma_sea)
    amber.database[e].join_sea(plasma_sea)
    amber.database[f].join_sea(plasma_sea)
    amber.database[g].join_sea(plasma_sea)
    amber.database[h].join_sea(plasma_sea)
    amber.database[i].join_sea(plasma_sea)
    boula_ship = ships.Ship.RegisterShip(creator_id=boula, where_is_it_created_id=plasma_sea,
                                         content_type=ships.ContentType.Text, txt_content="What??\nI'M REALLY A 1ST!")
    amber.database[plasma_sea].sail_ship_to_this_sea(boula_ship)
    amber.database[plasma_sea].members.extend([a, b, c, d, e, f, g, h, i])
    amber.database[plasma_sea].editors.extend([a, e, i])
    amber.database[plasma_sea].administrators.extend([b, c, d])
    # app = frontend.PostPreview(user_id=boula, post_id=boula_ship, destination_id=plasma_sea)
    app = frontend.AmberOcean(user_id=boula)
    manager = app.run()
else:
    boula = personal_docks.PersonalDock.RegisterAccount(name="Boula", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    boula = amber.database[boula]
    boula2 = personal_docks.PersonalDock.RegisterAccount(name="Boula222", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="whoneedsapassword", email='email@yahoo.com',
                                                        phone_number='01222222222')
    boula2 = amber.database[boula2]
    boula.add_email('email2')
    boula.add_link('linkedin', "linkedin.com/boulaza5")
    boula.add_special_field('f', "d")
    boula.add_family_member_relationship(boula2.id, personal_docks.FamilyRelationship.Brother)
    boula.add_relationship(boula2.id, personal_docks.RelationshipStates.Complicated, datetime.datetime(2014, 9, 28), datetime.datetime(2019, 9, 28))
    boula.add_living_place("Cairo", datetime.datetime(2014, 9, 28), datetime.datetime(2019, 9, 28))
    boula.add_education("m", "p", datetime.datetime(2014, 9, 28), datetime.datetime(2019, 9, 28))
    plasma_sea = seas.Sea.RegisterSea(creator=boula.id, name="Plasma Sea", description="I couldn't help but\nwhat?")
    plasma_sea = amber.database[plasma_sea]
    boula_ship = ships.Ship.RegisterShip(creator_id=boula.id, where_is_it_created_id=plasma_sea.id,
                                         content_type=ships.ContentType.Text, txt_content="What??\nI'M REALLY A 1ST!")
    boula_ship = amber.database[boula_ship]
    boula.export_to_xml()
    x = personal_docks.PersonalDock.load_from_xml()
    amber.database[x].export_to_xml('x.xml')
    plasma_sea.export_to_xml()
    x = seas.Sea.load_from_xml()
    amber.database[x].export_to_xml('x.xml')
    x = seas.Sea.load_from_xml('x.xml')
    amber.database[x].export_to_xml('f.xml')
    boula_ship.export_to_xml()
    x = ships.Ship.load_from_xml()
    amber.database[x].export_to_xml('x.xml')
    seanui.Group().run()
