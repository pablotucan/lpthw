def when_are_you_free(Monday, Tuesday, Wednesday):
    if Monday == 'Yes' and Tuesday == 'Yes' and Wednesday == 'Yes':
        print("You're free any day!")
    if Monday != 'Yes' and Tuesday != 'Yes' and Wednesday != 'Yes':
        print("You're not free any day!")
    if Monday == 'Yes' and Tuesday != 'Yes' and Wednesday != 'Yes':
        print("You're only free on Monday!")
    if Monday != 'Yes' and Tuesday == 'Yes' and Wednesday != 'Yes':
        print("You're only free on Tuesday!")
    if Monday != 'Yes' and Tuesday != 'Yes' and Wednesday == 'Yes':
        print("You're only free on Wednesday!")

Monday = input("Are you free Monday? Yes/No ")

Tuesday = input("Are you free Tuesday? Yes/No ")

Wednesday = input("Are you free Wednesday? Yes/No ")

when_are_you_free(Monday, Tuesday, Wednesday)
