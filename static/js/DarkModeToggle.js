function darkMode() {
  console.log("Dark Mode Running");
    localStorage.setItem('mode', (localStorage.getItem('mode') || 'light') === 'dark' ? 'light' : 'dark');
    if(localStorage.getItem('mode') === 'dark') {
      try {
        // DARKMODE     LIGHTMODE
        // bg-dark <-> bg-navy
        document.querySelector('.bg-dark').classList.replace('bg-dark', 'bg-navy')
      } catch(e) {}
      try {
        // DARKMODE     LIGHTMODE
        // bg-light <-> bg-dark
        document.querySelector('.bg-light').classList.replace('bg-light', 'bg-dark')
      } catch(e) {}
      try {
        // DARKMODE     LIGHTMODE
        // bg-white <-> bg-secondary
        document.querySelector('.bg-white').classList.replace('bg-white', 'bg-secondary')
      } catch(e) {}
      try {
        // DARKMODE         LIGHTMODE
        // navbar-light <-> navbar-dark
        document.querySelector('.navbar').classList.replace('navbar-light', 'navbar-dark')
      } catch(e) {}
      try {
        // DARKMODE      LIGHTMODE
        // text-dark <-> text-light
        document.querySelector('.text-dark').classList.replace('text-dark', 'text-light')
      } catch(e) {}
      try {
        // DARKMODE       LIGHTMODE
        // text-white <-> text-dark
        document.querySelector('.text-white').classList.replace('text-white', 'text-dark')
      } catch(e) {}
      try {
        // DARKMODE           LIGHTMODE
        // text-secondary <-> text-white
        document.querySelector('.text-secondary').classList.replace('text-secondary', 'text-white')
      } catch(e) {}
    }

    else {
      try {
        // DARKMODE     LIGHTMODE
        // bg-dark <-> bg-navy
        document.querySelector('.bg-navy').classList.replace('bg-navy', 'bg-dark')
      } catch(e) {}
      try {
        // DARKMODE     LIGHTMODE
        // bg-light <-> bg-dark
        document.querySelector('.bg-dark').classList.replace('bg-dark', 'bg-light')
      } catch(e) {}
      try {
        // DARKMODE     LIGHTMODE
        // bg-white <-> bg-secondary
        document.querySelector('.bg-secondary').classList.replace('bg-secondary', 'bg-white')
      } catch(e) {}
      try {
        // DARKMODE         LIGHTMODE
        // navbar-light <-> navbar-dark
        document.querySelector('.navbar').classList.replace('navbar-dark', 'navbar-light')
      } catch(e) {}
      try {
        // DARKMODE           LIGHTMODE
        // text-secondary <-> text-white
        document.querySelector('.text-white').classList.replace('text-white', 'text-secondary')
      } catch(e) {}
      try {
        // DARKMODE       LIGHTMODE
        // text-white <-> text-dark
        document.querySelector('.text-dark').classList.replace('text-dark', 'text-white')
      } catch(e) {}
      try {
        // DARKMODE      LIGHTMODE
        // text-dark <-> text-light
        document.querySelector('.text-light').classList.replace('text-light', 'text-dark')
      } catch(e) {}
    }

    var buttons = document.querySelectorAll('.btn');
    var heading = document.querySelectorAll('h1, h2, h3, h4');
    // btn-dark <-> btn-secondary
    for (var i = 0, len = buttons.length; i < len; i++) {
        console.log(buttons[i]);
        localStorage.getItem('mode') === 'dark' ? buttons[i].classList.replace('btn-dark', 'btn-secondary') : buttons[i].classList.replace('btn-secondary', 'btn-dark')
    }
    for (var i = 0, len = heading.length; i < len; i++) {
        console.log(heading[i]);
        localStorage.getItem('mode') === 'dark' ? heading[i].classList.replace('heading-section', 'heading-section-dark') : heading[i].classList.replace('heading-section-dark', 'heading-section')
    }
}
