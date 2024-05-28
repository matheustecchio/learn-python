// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew() {
    var newStudent = prompt("Enter with the new student's name: ")
    roster.push(newStudent)
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//
function remove() {
    var studentName = prompt("Enter with the student's name to be removed: ")
    roster.splice(roster.indexOf(studentName),1)
}


// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display() {
    console.log(roster)
}

// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
function menu() {
    var option = prompt("What you would like to do?\n1- Add a new student\n2- Remove a student\n3- Display the roster\n0 - Exit")
    if (option == 1) {
        addNew()
        menu()
    } else if (option == 2) {
        remove()
        menu()
    } else if (option == 3) {
        display()
        menu()
    } else if (option == 0) {
        exit
    } else {
        alert("Invalid option!")
        menu()
    }
}
var start = prompt("Would you like to use our web app?")
if (start == "Yes") {
    menu();
}