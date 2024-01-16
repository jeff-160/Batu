## General Syntax
`[keyword] [arg], [arg]...`

---

## Variables and Datatypes

### Types
- `ambasing` (boolean)
- `ambatukam` (integer)
- `ambatublou` (float)
- `ambatuexplode` (string)

### Declaring variables
- Usage: `[type] [name], [value]`
- Args: 
    - `type`: Datatype of variable
    - `name`: Name of variable
    - `value`: Value to store in variable

## amblokenu
- Deletes a variable
- Usage: `amblokenu [var]`
- Args:
    - `var`: Variable to delete

---

## Built-in Constants

### ambatugogetmesomesupper
- Stores the value of pi
- Usage: `%ambatugogetmesomesupper`

### itssofuckinghuge
- Stores the value of phi (golden ratio)
- Usage: `%itssofuckinghuge`

### ugheeeee
- Stores the value of e (euler's constant)
- Usage: `%ugheeeee`

---

## Referencing

### Variables
Prefixed by `$` identifier
- Examples:
    - `&variable`

### Built-in Constants
Prefixed by `%` identifier
- Examples:
    - `%ugheeeee`

### Keys and Mouse (GUI)
Prefixed by `&` identifier
- Examples:
    - `&KeyA`
    - `&KeySPACE`
    - `&POINTER`

---

## Logical Operators
Batu's logical operators are the same as Python's.

---

## Basic I/O

### yuwandisnut 
- Outputs a string to the console
- Usage: `yuwandisnut [text]`
- Args: 
    - `text`: String to output

### iwanit
- Request input from user
- Usage: `iwanit [var], [text]`
- Args:
    - `var`: Variable to store user input
    - `text`: Text to print to console when requesting input

---

## Labels
Can be used to simulate loops

### ambatubus
- Declares a label
- Usage: `ambatubus [name]`
- Args: 
    - `name`: Name of label

### yomemibus
- Jumps to line number of label
- Usage: `yomemibus [name]`
- Args:
    - `name`: Name of label

---
## Conditionals

### kazdasdanutanee
- Conditional block
- Usage : `kazdasdanutanee [condition], [span]`
- Args:
    `condition`: Condition to evaluate
    `span`: Will skip ahead to end of span if condition is false

---
## Additional Functions

### aauuhh
- Delays the program for an arbitrary time interval
- Usage: `aauuhh [interval]`
- Args: 
    `interval`: Time in milliseconds to delay program by

### ewww
- Exits the program
- Usage: `exit`

### ambatunat
- Stores a random floating point number in a variable
- Usage: `ambatunat [var]`
- Args:
    - `var`: Variable to store value into

### ambatufakinat
- Stores a random integer within a range in a variable
- Usage: `ambatufakinat [var], [min], [max]`
- Args:
    - `var`: Variable to store value into
    - `min`: Minimum value of random integer
    - `max`: Maxmimum value of random integer

### yesthankyousomuch
- Stores sine of a value in a variable
- Usage: `yesthankyousomuch [var], [value]`
- Args:
    `var`: Variable to store value into
    `value`: Value to apply sin to

### thankyou
- Stores cosine of a value in a variable
- Usage: `thankyou [var], [value]`
- Args:
    `var`: Variable to store value into
    `value`: Value to apply cos to

### thatmaybejustwhatineedtobus
- Stores tangent of a value in a variable
- Usage: `thatmaybejustwhatineedtobus [var], [value]`
- Args:
    `var`: Variable to store value into
    `value`: Value to apply tan to

### youneedtoholdit
- Stores length of a string into a variable
- Usage: `youneedtoholdit [var], [string]`
- Args:
    - `var`: Variable to store value into
    - `string`: String to get length of

### yesiam
- Stores index of a substring into a variable
- Usage: `yesiam [var], [string], [substr]`
- Args:
    - `var`: Variable to store value into
    - `string`: String to check index from
    - `substr`: Substring to get index of

### pseudomind
- Stores substring of a string into a variable
- Usage: `pseudomind [var], [string], [start], [end]`
- Args:
    - `var`: Variable to store value into
    - `string`: String to get substring from
    - `start`: Starting index of substring (inclusive)
    - `end`: Ending index of substring (exclusive)

--- 

## GUI

### omaygot
- Creates a new GUI window
- Usage: `omaygot [title], [width], [height]`
- Args
    - `title`: Title of window
    - `width`: Width of window
    - `height`: Height of window

### dontkam
- Updates the GUI window
- Usage: `dontkam`

### washthatass
- Clears the entire GUI window
- Usage: `washthatass`

### stretchdisass
- Resizes the GUI window
- Usage: `stretchdisass [width], [height]`
- Args:
    - `width`: New width of GUI window
    - `height`: New height of GUI window

### yuboutodestroydisass
- Closes the GUI window
- Usage: `yuboutodestroydisass`

### haurder
- Renders a rectangle on the GUI window
- Usage: `haurder [color], [x], [y], [width], [height]`
- Args:
    - `color`: Fill color of rectangle
    - `x`: X coordinate of rectangle
    - `y`: Y coordinateof rectangle
    - `width`: Width of rectangle
    - `height`: Height of rectangle

### bus
- Renders a circle on the GUI window
- Usage: `bus [color], [x], [y], [radius]`
- Args:
    - `color`: Fill color of circle
    - `x`: X coordinate of circle
    - `y`: Y coordinateof circle
    - `radius`: Radius of circle

### steven
- Renders a sprite on the GUI window
- Usage: `steven [path], [x], [y], [width], [height]`
- Args:
    - `path`: Relative file path of sprite image
    - `x`: X coordinate of sprite
    - `y`: Y coordinateof sprite
    - `width`: Width of sprite
    - `height`: Height of sprite

### vukvukvukvukvukvuk
- Render string of text on the GUI window
- Usage: `vukvukvukvukvukvuk [color], [text], [x], [y], [size]`
- Args:
    - `color`: Font color of text
    - `text`: Text to render
    - `x`: X coordinate of text
    - `y`: Y coordinateof text
    - `size`: Font size of text

### Event Variables
- Keys
    - State of key press
    - Usage: `&Key[A-Z | 0-9 | SPACE | ENTER]`
- Pointer
    - State of pointer press
    - Usage: `&POINTER`
- Pointer Coordinates
    - Current coordinates of pointer in GUI window
    - Usage: `&POINTER[X | Y]`