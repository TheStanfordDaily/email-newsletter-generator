/**
 * Go to step5.html in your web browser to get a feel for what is new.
 * 
 * What happens when you click submit? 
 * What happens is you click the link?
 * 
 */


// what is "clicks"? What data type? Where is it used?
let clicks = 0;

function set_featured_content() {
    /**
     * Step 5.1
     * 
     * Below is an example of how you can change a HTML element's text.
     * This isn't what we want to do in the end, but it is a good example to 
     * help us learn how Javascript and HTML work.
     * 
     * Why when you click submit does the text change? What in the below code
     * implements that functionality? Jumping ahead to step 5.2 may help with this
     * 
     * Why when you click the link does the page behave as it does (for this one it may be useful to 
     * take a look at how the link is implemented in html)?
     */

    // what is this?
    clicks = clicks + 1;

    /**
     * Step 5.2
     * 
     * What is "innerHTML"?
     * What does the below line do?
     * What is the `${}` thing?
     * 
     * https://www.w3schools.com/jsref/prop_html_innerhtml.asp
     * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
     */
    document.getElementById("featured_content_headline_link").innerHTML = `Clicked ${clicks} times!`;
     
    /**
     * Step 5.3
     * 
     * Now that we understand how the above code works, we can replace it with 
     * code that will replace the link's text/innerHTML with the user's input to the
     * featured content headline textarea once the submit button is pressed. You may 
     * find referring back to step4.js to be helpful.
     * 
     */

    /**
     * Step 5.4
     * 
     * Woah, that's cool! We're pretty close to getting the core functionality of this form working.
     * To continue towards that goal, make it so that the user's inputs to each of the other
     * textarea inputs will do something reasonable when the submit button is clicked!
     * You'll have to modify step5.html in addition to modifying this file.
     * 
     * Hints: for the featured content link, try altering the <a> tag's href. 
     * For the image, check out the <img> tag! Consider an h1/h2/h3... for the author names, 
     * Consider using a <p> tag for the excerpt. 
     * 
     * Great! Your form is almost there!
     */

    /**
     * Step 5.5
     * 
     * Styling! Now that we have everything in place, have some fun with styling--
     * make this newsletter look as beautiful as you can make it :).
     * 
     * You can start by creating a step5.css file, and copying over the
     * contents of step1.css. Then, remember to change step5.html to use step5.css instead
     * of step1.css.
     * 
     * Also, remember, we can reuse the id selectors which we created!
     */
}