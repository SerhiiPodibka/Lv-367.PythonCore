def reverse(st):
    splitted = st.split()
    reversed = splitted[-1::-1]
    st=' '.join(reversed)
    return st
