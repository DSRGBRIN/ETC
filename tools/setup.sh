sudo apt update
sudo apt install openjdk-17-jdk -y
sudo apt-get install unzip
wget https://hyperledger.jfrog.io/artifactory/besu-binaries/besu/24.1.1/besu-24.1.1.zip
unzip besu-24.1.1.zip
rm besu-24.1.1.zip
echo "Testing Besu:"
besu-24.1.1/bin/besu operator --help
echo "Testing Java:"
java --version
echo "Setup is Done!"
echo "# Next steps:"
echo "echo \"alias besu=\\\"$HOME/besu-24.1.1/bin/besu\\\"\" >> .bashrc"
echo "source .bashrc"
echo "besu --help"
