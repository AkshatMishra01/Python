#Q 1) Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. Then, plot the arrays as vectors using the fuction Plotvec2 and find the dot product:

# Answer)

a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))
