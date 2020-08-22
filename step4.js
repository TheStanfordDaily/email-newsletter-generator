/**
 * Try "running" the code below by going to step4.html
 * in your web browser, filling out the "Featured content headline"
 * field and then pressing the submit button. What do you see?
 * Why do you see it?
 * 
 */
function set_featured_content() {
    /**
     * Step 4.1
     * 
     * What is "document"? What is "getElementById"?
     * where does "featured_content_headline_text" come from (why are we using it?
     * what if we change it?)
     * 
     * What is "value"? What if we remove it? Can we replace it with something else?
     * 
     * https://www.w3schools.com/jsref/dom_obj_document.asp
     * https://www.w3schools.com/jsref/met_document_getelementbyid.asp
     * https://www.w3schools.com/jsref/prop_textarea_value.asp
     */
    alert(document.getElementById("featured_content_headline_text").value);

    
    /**
     * Step 4.2
     * 
     * Are these lines different from the above lines?
     * Consider that question from the perspective of the website user, then from
     * the perspective of the developer (you) and finally from the perspective of the
     * computer. 
     * 
     */
    let featuredContentHeadlineTextValue = document.getElementById("featured_content_headline_text").value;
    alert(featuredContentHeadlineTextValue);

    /**
     * Step 4.3
     * 
     * featuredContentHeadlineTextValue is a "string"
     * Since it is a piece of data with type string, we can perform string operations on it
     * What do each of these operations do? How can you verify that your answers are correct? 
     */

    let weirdString1 = featuredContentHeadlineTextValue + featuredContentHeadlineTextValue;
    let weirdString2 = `${featuredContentHeadlineTextValue}`; // why `${}` useful?
    let weirdThing2 = featuredContentHeadlineTextValue.length;

    /**
     * Step 4.4
     * 
     * Now, finish this code by getting and logging (console.log or alert; your choice) 
     * the rest of the form inputs!
     */
}