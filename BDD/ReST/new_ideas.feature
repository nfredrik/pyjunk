￼Feature: Basic REST Interactions
Background:
  Given the server knows about the following resources
      |type   |path                    |
      |api    |/hue/api                |
      |light  |/hue/light/id/{id}      |
      |nonexistent|/hue/does/not/exist |
 
And the server knows about the following mime types
      |HTML   |text/html                       |
      |Cj     |application/vnd.collections+json|

 