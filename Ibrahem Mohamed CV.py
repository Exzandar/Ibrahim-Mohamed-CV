summary = '''
[+] I’m a geek who loves everything related to cyber security.
[+] I started my journey 4 years ago by self-learning and online courses. 
[+] I participated in many competitions till I got into top 10 Egyptians in HackTheBox and many CTFs sites. 
[+] I found bugs in many web applications that provide services related to communication, shopping,
    booking and governments. 
[+] I’m able to do vulnerability assessment and penetration testing for network and web applications.\n'''

print(summary)

sections = '''
[1] -> Contact Information.
[2] -> Experience.
[3] -> Self-Learning and Online Courses.
[4] -> Education.
[5] -> Soft and Technical Skills.
[6] -> Exit.
'''

print(sections)

selection = {
    "information": '''
    -> Name: [ Ibrahim Mohamed Ibrahim. ]
    -> Address: [ Egypt, Alexandria. ]
    -> Phone-Number: [ +201122359610, +201550301796. ]
    -> G-mail: [ Ibrahim98Mohamed98@gmail.com . ]
    -> LinkedIN: [ https://www.linkedin.com/in/exzandar/ . ]
    -> Personal Blog: [ https://exzandar.home.blog . ]''',

    "education": '''
       -> Assiut UNIVERSITY – Egypt, Assiut.
       -> Bachelor of Accounting & Business Management [English-Section], Sept 2020
       -> Economics, Politics, Business management and Accounting.''',

    "skills": '''
       [ web application penetration testing, network penetration testing, vulnerability assessment, windows, Linux, 
       CTF player, python programming, researches, cryptography, scripting language, social engineering, 
       manual and automated testing, problem solving, familiar with almost all tools and frameworks ]''',

    "objective": '''
       Smart and hard-working penetration tester, skilled in Web App Pen-Testing, Network Pen-testing
       and Vulnerability Assessment, seeking to join your company to work in a collaborative environment 
       with intelligent people where we can perform penetration tests together on all products and systems 
       In a creative, smart and real methods manually or with automated tools and report everything happening
       In details to reach customer satisfaction and build a trusted reputation.''',

    "courses": '''
       -> TryHackMe Offensive Security – 2022.
       -> JR Penetration Tester – 2022.
       -> eWAPT elearnSecurity – 2020.
       -> CEH v10 elearnSecuriy - 2020.
       -> Pen-Testing & Ethical Hacking – 2018.
       -> CCNA – 2018.
       -> Competitive Programming and Problem Solving – 2017.
       -> Cryptography – 2017.''',

    "experience": '''
       
       ^ BugCrowd ^ [ Bug Hunter, May 2022 – Present ]\n
            •	Doing bug hunting, report vulnerabilities and being listed in HOFs (US Government, US Environmental Protection Agency).
       
       ^ Part-Time Projects [Free-Lancing] ^ [ Penetration tester, April 2022 – Present ]\n
            •	Training in real projects with experienced penetration testers to sharp my skills, my experience and learn to build methodologies, create reports and plans.
            •	Learn from the ideas of experienced penetration testers and bug hunters.
            •	I found bugs in many web applications that provide services related to communication, shopping, booking, financial and governments.

       ^ CTF Player, Machines Attacker and Security Content Writer ^ [ Geek and fast learner, September 2018 – Present ]\n
            •	I started my hard journey 4 years ago with hard practice, ambition and passion.
            •	Hard working has led me to be into top 10 Egyptians on HackTheBox.
            •	I solved more than 300 CTF challenges and more than 30 machines in different platforms.
            •	I started to write my write-ups, walk-throughs in 2019 to share my knowledge and techniques with others
                via my personal blog [https://exzandar.home.blog] and my content reached to 10,000+ geek around the world!

       ^ Student Activities in university ^ [ IT specialist, June 2016 – July 2018 ]\n
            •	I was the manager of IT committee in Enactus AU and we have managed to create our website
                to help more than 300 members that year to register in Enactus and get all their IT-Work related done!
            •	I was IT specialist in SMS AU for practical courses, and I’ve managed to make 215 members connected 
                to a network with only a USB flash internet, through network skills.
            •	I learned problem solving in FCI AU and participated in many problem-solving competitions so I became a mentor.
            '''}

while True:
    choice = int(input("\nChoose Section Number between 1 and 6: "))
    if choice not in range(1, 7):                 # verify selection
        print("\nInvalid Choice!")
        continue
    elif choice == 1:                               # contact information section
        print(selection["information"])
    elif choice == 2:                               # Experience.
        print(selection["experience"])
    elif choice == 3:                               # Self-Learning and Online Courses
        print(selection["courses"])
    elif choice == 4:                               # Education
        print(selection["education"])
    elif choice == 5:                               # Soft and Technical Skills
        print(selection["skills"])
    else:
        verify = input("Are you sure you want to exit? Y or N: ")
        if verify in ["no", "No", "N", "n", "NO", "nO"]:
            continue
        else:
            break
exit(1)
