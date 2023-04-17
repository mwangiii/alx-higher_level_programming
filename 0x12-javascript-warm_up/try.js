//#1

let num = 10 + 2;

if (num > 2 && num < 20) {

    console.log("TRUE");        

} else {

   console.log("FALSE"); 

}

//output:- TRUE



//#2

let user = 'employee';

if (user === 'guess') {

    console.log("Login Denied");

} else if(user === 'employee') {

    console.log("Sucessfully Logged in");   

}

//output:- Sucessfully Logged in





//#3

const myName = "Robin";

let lengthName = myName.length;

if (lengthName > 5){
    alert ("More than 5")
}else if (lengthName >= 5) {
    alert ("Exat 5 letters")
}else {
    alert ("Less than 5 letters")
}
//output:- Exat 5 letters
