firebase.auth().onAuthStateChanged(function(user) {
	if (user) {
	  // User is signed in.

	} else {
	  // No user is signed in.

	}
  });

function login() {
	var userEmail = document.getElementById("email_field").value;
	var userPass = document.getElementById("password_field").value;
	window.alert("Success");
	firebase.auth().signInWithEmailAndPassword(userEmail, userPass)
	.then((userCredential) => {
		// Signed in
		var user = userCredential.user;
		
		// ...
	})
	.catch((error) => {
		var errorCode = error.code;
		var errorMessage = error.message;
		window.alert("Error: ");
	});
}