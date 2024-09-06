# Send2TV

This client works alongside [Wireless File Manager](https://github.com/visnkmr/wfm)

---

## Usage
Y'all can figure it out :wink:

---

## History

The default web client of WFM doesn't allow for multiple file selections.
That's why I had to come up with this thing.
Specifically handy for multiple large-file transfers to TV (iykyk).

[Localsend](https://localsend.org/) app on FireTV OS for some reason glitches and doesn't allow to change the download location. It forced me to use WFM.

---

## Future Work
The WFM was built on TCP which makes it pretty slow by nature.
Parallel connections is most definitely possible but we have the bottleneck of USB transfer speeds for budget & mid-end Smart TVs.
Might build a client running on UDP for speed gains.

If you don't have that bottleneck constraint, You most proabably won't even require this app assuming you got a good amount of internal storage, thereby, the app you should use is Localsend.