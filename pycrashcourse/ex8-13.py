def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last 
    for key, value in user_info.items():
        profile[key] = value
    return profile


chad = build_profile("Chad", "Tennent", location = "portland", age = 30, hair = "blonde")
Sabrina = build_profile("Sabrina", "Cadena", Location = "portland", age = 19, hair = "purple")
print(chad['first name'] + " loves " + Sabrina['first name']) 


