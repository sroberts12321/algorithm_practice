num_of_stars = int(input("How large would you like the base of the pyramid to be? Odd numbers only: "))

star_tracker = 1

space_tracker = int(((num_of_stars - 1) / 2))


while star_tracker <= num_of_stars:
	print((" " * space_tracker) + ("*" * star_tracker))
	star_tracker += 2
	space_tracker -= 1

#input 17 for an identical pyramid
#pyramid for reference
print(
"""
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************

"""
)