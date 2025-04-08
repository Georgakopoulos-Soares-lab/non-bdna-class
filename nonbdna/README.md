# NON B-DNA Detection tools

Let's clone some packages important for non b-dna detection:

```
export CLASS=nonbdna_class
mkdir -p && cd $CLASS
git clone git@github.com:abcsFrederick/non-B_gfa.git
```

After we have cloned the repository we need to compile it using:

```
make
```

Finally, we will create an alias, so we can access the tool from anywhere on our
computer:

```
echo "alias gfa=$(readlink -f ./gfa)" >> ~/.bashrc
chmod +x ./gfa
```

Let's restart the shell:

```
source ~/.bashrc
```

Time to test it! Type:

```
cd && ./gfa
```

You are ready to detect non b-dna!
