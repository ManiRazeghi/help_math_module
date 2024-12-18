# How to use help_math module
### `Introduction` :<p>This module have One decorator to check function's `argument` and one function to calculate `sqrt` of intiger number type.<p>
### For use of this model you shuld import the module:
```python
  import help_math
```
---
### check_type_input
This `decorator` is use to check function's input `type`.
- ### for example:
  - ```python
      from help_math import check_type_input

      @check_type_input([int, int])
      def simple_minus(num1: int, num2: int) -> int:
          return num1 - num2
      
      print(simple_minus(10, 8)) # out_put: 2
      print(simple_minus(12.5, 2))# raise TypeError -> inputer "12.5" is not type as int
    ```
  
  - ```python
      from help_math import check_type_input

      @check_type_input([str, str])
      def simple_add(word1: str, word2: str) -> str:
          return word1 + word2
      
      print(simple_add('a', 'b')) # out_put: 'ab'
      print(simple_minus(0, 2))# raise TypeError -> inputer "0" is not type as str
      print(simple_minus('exam', 100))# raise TypeError -> inputer "100" is not type as str
    ```
---

### ultra_sqrt
This `function` is use to sqrt number and raise ValueError when number is negative
- ### for example:
  - ```python
      from help_math import ultra_sqrt

      print(ultra_sqrt(16))# out_put: 4
      print(ultra_sqrt(10))# out_put: 3.3
      print(ultra_sqrt(-25))# raise ValueError -> -25 is negative
    ```
  
