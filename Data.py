from rcapi import auth, factory
creds = auth.fj_login()['Token']
robots = factory.factory_list(creds, factory.make_search_body(search="", player=None))
print(robots)