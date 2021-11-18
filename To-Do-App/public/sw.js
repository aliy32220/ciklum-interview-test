const CACHE_KEY = 'todo-v1';
const filesToCache = [
  '/',
  'index.html',
  'img/'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_KEY)
      .then(cache => {
        return cache.addAll(filesToCache);
      })
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(cacheList => {
      return Promise.all(
        cacheList.map(cache => {
          if (cache !== CACHE_KEY) {
            return caches.delete(cache);
          }
        })
      );
    })
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request)
      .then((response) => {
        return response || fetch(e.request);
      }))
});
