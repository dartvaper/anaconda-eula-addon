.PHONY: all clean

SQUASHFS_PATH = "http://mirror.centos.org/centos/7.2.1511/os/x86_64/LiveOS/squashfs.img"

all: squashfs.img new-squashfs.img

squashfs.img:
	wget -q $(SQUASHFS_PATH)

new-squashfs.img: squashfs.img eng.txt
	unsquashfs -d squashfs squashfs.img
	mkdir squashfs/LiveOS/rootfs
	mount squashfs/LiveOS/rootfs.img squashfs/LiveOS/rootfs/
	cp -r anaconda_eula_addon squashfs/LiveOS/rootfs/usr/share/anaconda/addons/
	mkdir squashfs/LiveOS/rootfs/usr/share/anaconda-licenses/
	cp *.txt squashfs/LiveOS/rootfs/usr/share/anaconda-licenses/
	umount squashfs/LiveOS/rootfs/
	rm -rf squashfs/LiveOS/rootfs
	mksquashfs squashfs $@ -root-owned

eng.txt:
	cp LICENSE $@
	
clean:
	rm -rf squashfs
	rm -f *.img
	rm -f eng.txt
