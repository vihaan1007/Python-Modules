import warnings

#warn

warnings.warn("This feature is deprecated(to be removed)", DeprecationWarning)
warnings.warn("Generic warning", UserWarning)
warnings.warn("Behaviour will change", FutureWarning)
warnings.warn("Suspicious runtime behavior", RuntimeWarning)
warnings.warn("Suspicious syntax", SyntaxWarning)
warnings.warn("Generic warning", ImportWarning)

#filter

warnings.filterwarnings("ignore")#ignore
warnings.filterwarnings("ignore", category=DeprecationWarning)#ignore specific




warnings.filterwarnings("once")#once
warnings.filterwarnings("always")#Always
warnings.filterwarnings("default")#Python default behaviour




#Convert warning to exception

print("Before")

warnings.filterwarnings("error")
warnings.warn("This will raise exception")#Usererror

print("After")#Nothing because We have a User define error





