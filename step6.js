/**
 * Step 6.2
 * 
 * Copy over your step5.js into here!
 * 
 * You can/should delete anything that's not needed, like "clicks"
 * or any alerts and console.logs that may be remaining.
 */

 /**
  * Step 6.3
  * 
  * Create and implement a function for your second button to call here!
  * 
  * In implementing this function, a good practice is to start from a simple,
  * working (but not "correct") version, and then building from there.
  * This process of starting from a working version and incrementally changing your
  * code is one which many developers use all the time.
  * 
  * For example, I'd start with a function which calls
  * alert("This function was called!") and see that this alert behaves as expected.
  * 
  * Then I could get the innerHTML of the "output_fields" div, and log that string so that
  * we know that we can "get" it.
  * 
  * Next, I would create a new div and create a text area with some unique id (like "email_output")
  * in the html file
  * 
  * Finally, I would set the value of this textarea to be the innerHTML string that we got
  * from the "output_fields" div.
  * 
  * Then, as a final test, I would copy the contents of that textarea, create a new
  * html file, paste those contents in, and then open that html file up in your
  * browser. Hopefully you'll see the generated newsletter! 
  * 
  * Note that your css probably won't show up--don't worry about this for now!

  * If you're successful, that's amazing!!! You just created a website that can generate
  * new websites!! I wonder if you can now make a website that can create a website
  * that can create new websites...? That'd be like inception or something... (it's definitely
  * possible--if you have spare time, I encourage you to try it out! Actually, the idea of
  * creating a program that can reproduce itself is a fun "game" that a lot of well
  * known programmers like to play. Such a program is called a "quine").
  * 
  * The example() function will give some hints of some things you can do.
  * Go to console in your web browser and call example() to see what it does!
  */

  function example(){
      let output_string = document.getElementById("example_input").innerHTML;
      console.log("output string is: ", output_string);
      document.getElementById('example_output').value = output_string;
  }