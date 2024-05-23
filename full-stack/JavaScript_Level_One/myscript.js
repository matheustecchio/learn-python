var firstName = prompt("Enter with your first name: ")
var lastName = prompt("Enter with your last name: ")
var age = prompt("Enter with your age: ")
var height = prompt("Enter with your height(cm): ")
var petName = prompt("Enter with your pet name: ")

if ((firstName[0] == lastName[0]) && (age >= 20 && age <= 30) && height >= 170 && petName[petName.length-1]) {
    alert("Hello Spy")
} else {
    alert("Nothing to show")
}