#გამოიყენეთ შემდეგი საკვალიფიკაციო კრიტერიუმები: პირი უნდა იყოს მინიმუმ 18 წლის მართვის მოწმობის მისაღებად. თუ პირი 18 წლამდეა, მას არ შეეძლება მართვის მოწმობის აღება. თუ პირი არის 18 წლის ან მეტი, მას უნდა ჰქონდეს მინიმუმ 1 წლიანი მართვის გამოცდილება, რომ დაშვებული იყოს მართვის მოწმობის აღებისთვის.
age = input(" age: ")
experience = input(" experience: ") 

if int(age) >= 18 and int(experience) >= 1:
    print('you can take driver license test')
else:
    print('you cannot take driver license test')
