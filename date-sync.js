/* date-sync.js — estado de data partilhado entre páginas via ?d=YYYY-MM-DD na URL.
   Sem isto: cada página usa sempre LATEST_DATE. Com isto: uma página pode fixar
   um dia (setDay) e propagar essa escolha para as outras ao navegar. */
const DateSync = {
  read(){
    const p = new URLSearchParams(location.search);
    const d = p.get('d');
    return (d && /^\d{4}-\d{2}-\d{2}$/.test(d)) ? d : null;
  },
  write(date){
    const url = new URL(location.href);
    url.searchParams.set('d', date);
    history.replaceState(null, '', url);
  },
  wireNav(date){
    document.querySelectorAll('.nav-item').forEach(a => {
      const u = new URL(a.getAttribute('href'), location.href);
      u.searchParams.set('d', date);
      a.href = u.pathname + u.search;
    });
  }
};
