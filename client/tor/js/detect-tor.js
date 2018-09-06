// This user agent string matches Tor Browser 8 or Firefox Quantum (on desktop)
const TBB_UA_REGEX = /Mozilla\/5\.0 \((Windows NT 6\.1|X11; Linux x86_64|Macintosh; Intel Mac OS X 10\.13|Windows NT 6\.1; Win64; x64); rv:[0-9]{2}\.0\) Gecko\/20100101 Firefox\/([0-9]{2})\.0/


const is_likely_tor_browser = function () {
	return (
		// Tor Browser has the Tor/FF UA string
		window.navigator.userAgent.match(TBB_UA_REGEX) &&
		// Tor Browser always reports a GMT timezone
		new Date().getTimezoneOffset() == 0 &&
		// Tor Browser always reports device dimensions being the same
		// as window dimensions -- this is *very* unlikely to be true in any
		// other desktop browser, given window chrome and toolbars
		window.screen.width == window.innerWidth &&
		window.screen.height == window.innerHeight
	)
}


// Adjust <html> element classes according to tor detection
document.documentElement.classList.remove('no-js')
document.documentElement.classList.add('js')
document.documentElement.classList.add(is_likely_tor_browser() ? 'tor' : 'no-tor')


// Warn about using Javascript and not using Tor Browser
document.addEventListener("DOMContentLoaded", () => {
	const useTorBrowser = document.getElementById('js-use-tor-browser')
	const instances = document.getElementById('js-instances')
	const body = document.body

	if (is_likely_tor_browser()) {
		/* If the source is using Tor Browser, we want to encourage them to turn Tor
			Browser's Security Slider to "High", which enables various hardening
			methods, including disabling Javascript. Since JS is disabled by turning
			the Security Slider to "High", this code only runs if it set to another
			(less hardened) setting. */
		let torWarning = document.getElementById('js-tor-warning')
		torWarning.classList.remove('tor-warning--hidden')
		torWarning.setAttribute('aria-hidden', 'false')
		//  hides the warning to use tor, since users already have it
		useTorBrowser.classList.add('tor-warning--hidden')
		useTorBrowser.setAttribute('aria-hidden', 'true')
		// adds class to body that disables scrolling
		body.classList.add('no-scroll')
		// Tell instances and updates that there's a warning
		// so that homepage styles are adjusted
		if(instances) {
			instances.classList.add('instances--tor-warning')
		}

		let torWarningClose = document.getElementById('js-tor-warning-close')
		const closeUseTorBrowser = document.getElementById('js-tor-warning-close')

		closeUseTorBrowser.addEventListener('click', () => {
			torWarning.classList.add('tor-warning--hidden')
			// hides warning for screen readers
			torWarning.setAttribute('aria-hidden', 'true')
			body.classList.remove('no-scroll')
			if(instances) {
				instances.classList.remove('instances--tor-warning')
			}
		})
	} else {
		// If the user is not using Tor Browser, we want to encourage them to do so.
		useTorBrowser.classList.remove('tor-warning--hidden')
		useTorBrowser.setAttribute('aria-hidden', 'false')
		body.classList.add('no-scroll')
		if(instances) {
			instances.classList.add('instances--tor-warning')
		}

		const closeUseTorBrowser = document.getElementById('js-use-tor-browser-close')
		closeUseTorBrowser.addEventListener('click', () => {
			useTorBrowser.classList.add('tor-warning--hidden')
			useTorBrowser.setAttribute('aria-hidden', 'true')
			body.classList.remove('no-scroll')
			if(instances) {
				instances.classList.remove('instances--tor-warning')
			}
		})
	}
});
