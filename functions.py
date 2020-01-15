running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]    
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]
all_the_kids = [running_kids, swinging_kids, sliding_kids, swinging_kids]
activities = ["ran", "swung", "slid", "hid"]

def kid_activity(kids_lists, activity):
    for kid_list in kids_lists:
        for kid in kid_list:
            for activity in activities:
                print(f'{kid} {activity} today!')


kid_activity(all_the_kids, activities)