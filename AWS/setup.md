# TLDR - Setting up an AWS instance and cloning a git repository with a ssh key

---

## Topics
- [Starting things up](#starting-things-up)
- [What's next? Let's configure a SSH key](#whats-next-lets-configure-a-ssh-key)
- [Generating you SSH key](#generating-you-ssh-key)
- [Cloning a GitHub Repo with your key](#cloning-a-github-repo-with-your-ssh-key)

---

## Starting things up
- First, start your lab session clicking on "start lab" (too easy huh)
- On the upper left corner, click on "AWS" icon;
- On "show all services" section, find EC2 and, in the next page, click on execute instance
- Choose Red Hat Enterprise Linux as your Application Image
- Select Vockey as your pair of keys (login)
- Make sure you are allowing SSH traffic (I choose from anywhere)
- Now you can execute your instance

## What's next? Let's configure a SSH key
- You will see a feedback message confirming the creation
- Click on the instance id, and open your VM details by clicking on its id again
- Copy its IPv4 Public IP
- Assuming you selected vockey key pair and have opened TCP port 22 (automatically) in the instance's security group. On your AWS terminal, run the following command

```bash
ssh -i ~/.ssh/labsuser.pem ec2-user@<public-i\p>
```

- Change <public-ip> with the IPv4 public IP you copied
	
- Reference: https://labs.vocareum.com/web/3112326/2695337.0/ASNLIB/public/docs/lang/en-us/README.html#ssh

## Generating you SSH key
- Just type
	
```bash
ssh-keygen
```
	
- Press enter until the key's randomart image is generated
- An important thing to mention is that will be prompted to you the following question
	
> Enter file in which to save the key (/home/ec2-user/.ssh/id_rsa)

- This path between parentheses is the path where your ssh key is stored
- To check your brand new key, run the following command

```bash
cat <ssh key pat\h>
```
	
- Since our path is the one inside the parentheses, then we should run

```bash
cat /home/ec2-user/.ssh/id_rsa.pub
```

- Copy the whole key. It's big, isn't it?

## Cloning a GitHub Repo with your SSH key
- Now, create a GitHub repository or create in a version control system of your preference
- Go to settings, select "deploy keys"
- Click on "add deploy key"
- Select "allow write access"
- In your repo's github page, clone it by using the ssh command

```bash
git clone git@github.com:<repo\'s url>
```

- To install git on your VM, type

```bash
sudo dnf install git
```

- Confirm what needs to be confirmed and wait until it's installed
- Now you are capable of cloning your repo and making changes on it 

## Running a Hello World example in Java
- Install Red Hat OpenJdk using the following command

```bash
sudo yum install java-21-openjdk-devel
```

- Create a Hello.java file using cat command

```bash
cat > Hello.java << HELLO
```
- Then you will be prompted to enter your text until you type `HELLO`

```bash
> public class Hello {
>	public static void main(String[] args) {
>		System.out.println("Hello, world! :^)");
>	}
> }
> HELLO
```

- "<< HELLO" is used to set an EOF, so you will need to type "HELLO" on the last line to end your Hello.java file
- Now, compile your file with

```bash
javac Hello.java
```

- Now, let's run it! :^)

```bash
java Hello

>> Hello, World!
```