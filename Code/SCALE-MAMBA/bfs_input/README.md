# SCALE-MAMBA Input 


SCALE-MAMBA get input from stdin by default (without using C++ code to overwrite input).

For example, the following code will read a secret int from stdin:

sint.get_private_input_from(0)


Linux pipe | can connect output content from another program (i.e. cat) and become
stdin input for another program. 

We use Linux cat to display content of input file and use Linux pipe to redirect to SCALE-MAMBA:

```
cat input.txt | SCALE-MAMBA-Player.x
```

### SCALE-MAMBA

Go to SCALE-MAMBA directory

```
cd SCALE-MAMBA
```
The test code is under the directory 
Programs/bfs_input 

### Example input 

280_AS_LCC_IPv6L.edgelist
File containing edges, each line contains src and dest node 

Test to see the input file

```
cat Programs/bfs_input/280_AS_LCC_IPv6L.edgelist
```

### Instructions

Launch 3 terminals on the Linux machine (can be same or different machines)

terminal 0:

Party 0

Explaination of the command:
- using Linux cat command to display content of the input file 
```
- cat Programs/bfs_input/280_AS_LCC_IPv6L.edgelist  
```
- the cat output is sent to SCALE-MAMBA as stdin using Linux pipe | 
```
cat Programs/bfs_input/280_AS_LCC_IPv6L.edgelist |  ./Player.x  
```
- SCALE-MAMBA run using verbose level 1 to show print_ln(...), the 0 in the command line represent party 0 (terminal running on terminal 1 ) 
```
 ./Player.x -verbose 1 0 Programs/bfs_input
```


terminal 1:

Party 1

```
cd SCALE-MAMBA
 ./Player.x -verbose 1 1 Programs/bfs_input
```

terminal 2:

Paryt 2

```
cd SCALE-MAMBA
 ./Player.x -verbose 1 2 Programs/bfs_input
```

You should see the following output from terminal 1

```
melody@BunnyLinux:~/SCALE-MAMBA$ cat Programs/bfs_input/280_AS_LCC_IPv6L.edgelist |  ./Player.x -verbose 1 0 Programs/bfs_input
+ '[' '' == 1 ']'
+ ./PlayerBinary.x -verbose 1 0 Programs/bfs_input

No FHE Factories 2
Port Num Base 5000
Portnums :
Verbose 1
maxI = 0
(Min,Max) number of ...
	(0,infty) multiplication triples
	(0,infty) square pairs
	(0,infty) bits

0
127.0.0.1
Player1.crt
P1
1
127.0.0.1
Player2.crt
P2
2
127.0.0.1
Player3.crt
P3


p=340282366920938463463374607431768211507

Using Mod2Engine system for the binary circuit processing
  - This uses Replicated sharing mod 2

Opening file Programs/bfs_input/bfs_input.sch
Number of online threads I will run in parallel =  1
Number of program sequences I need to load =  1
Loading program 0 from Programs/bfs_input/bfs_input-0.bc
All connections now done
Setting up threads
I am player 0 in thread 1
I am player 0 in thread 2
I am player 0 in thread 3
I am player 0 in thread 20000
Waiting for thread 0 to be ready
...
nnel 0 : Input channel 0 : Input channel 0 : Input channel 0 : Input channel 0 : Input channel 0 : Input channel 0 : Input channel 0 : Input channel 0 : the first 10 edges
[0]: src = 14618, dst = 1273
[1]: src = 14618, dst = 16509
[2]: src = 14618, dst = 1257
[3]: src = 14618, dst = 7908
[4]: src = 13101, dst = 3257
[5]: src = 13101, dst = 6695
[6]: src = 13101, dst = 29551
[7]: src = 13101, dst = 3356
[8]: src = 13101, dst = 12731
[9]: src = 13101, dst = 1200
Compiler: ./compile-mamba.py -A -n -r -u -s Programs/bfs_input
Waiting for all clients to finish
Waiting for all clients to finish
	Thread 0 terminating
Exiting online phase : 0
Sent 2788 elements in 2778 rounds
<b3m4>
Number instructions executed in online thread 0 is 11249
</b3m4>
Batch Size = (1048576,64)
	Per Second = 2.58312e+06
```