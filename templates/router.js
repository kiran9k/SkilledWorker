/*jshint esversion: 6 */

import Vue from 'vue';
import VueRouter from 'vue-router';


import indexPage from '../templates/main/index.vue';
import searchPage from '../templates/main/search.vue';


Vue.use(VueRouter);

const routes = [
    { path: '/', name: 'Home', component: indexPage, alias: '/' },
    { path: '/search', name: 'Search', component: searchPage, alias: '/search' },
];



var router = new VueRouter ({
    routes: routes,
    mode: 'history',
    linkActiveClass: 'active'
});


export default router;
