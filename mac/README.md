## Mac Installation

Instructors: `Ilias Georgakopoulos-Soares izg5139@psu.edu`

Please for any question contact Nikol in the following email: `nmc6088@psu.edu`.

With Mac computers many things are already made to us available from the 
unix ecosystem.

## Installing Homebrew

Let's open the macOS Terminal and type:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Installing Git

Let's install some utilities:

```
brew install wget git
```

Check your git installation was succesful by typing:

```
git --version
```

If you see git with a version number it means it has been succesful! ✅

Let's install your github CLI:

```
brew install gh
brew upgrade gh
```

## Installing Python

To install python we will use a package manager.

In this class we will install Micromamba.

In Mac we can install micromamba via homebrew:

```
brew install micromamba
```

After the installation is complete, verify that it was succesful:

```
micromamba --version
```

Now let's create a virtual environment:

```
export CLASS="nonbdna"
micromamba create -n $CLASS python=3.12
```

You have to click Y[Yes] when prompted.

Now let's activate our environment by running:


```
micromamba activate nonbdna
```

Let's verify that python has succesfully been installed by typing:

```
python --version
```

If you see Python written on your terminal, it means the installation 
was succesful!
