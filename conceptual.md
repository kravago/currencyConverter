### Conceptual Exercise

Answer the following questions below:

1. What are important differences between Python and JavaScript?
   * In a web application, Python is used for the backend and Javascript is used for the front end, but can be used on the server side as well. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  * You can check to see if the key "c" is in the dictionary and then access it. The other way is to use the function get() which can return a default value or None to keep your program running

- What is a unit test?
  * A unit test will test components of a web application's code. For example, a test that tests a function to make sure that function is working the way it should.

- What is an integration test?
  * An integration test will test how multiple components work together. They may be harder to create than unit tests.

- What is the role of web application framework, like Flask?
  * A web framework handles the routing of requests. When a route is requested from the client, Flask will help with returning the webpage requested.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  * The URL query parameters are good for when the client wants to send data to the server, such as when a form is being submitted. Having parameters in a route URL is best when you are trying to display pages that use the same template but with information from other data structures. 

- How do you collect data from a URL placeholder parameter using Flask?
  *
- How do you collect data from the query string using Flask?

- How do you collect data from the body of the request using Flask?

- What is a cookie and what kinds of things are they commonly used for?

- What is the session object in Flask?

- What does Flask's `jsonify()` do?
