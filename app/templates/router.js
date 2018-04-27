/*jshint esversion: 6 */

import Vue from 'vue';
import VueRouter from 'vue-router';


import indexPage from '../templates/main/index.vue';
import searchPage from '../templates/main/search.vue';
import showProfilePage from '../templates/main/profileView.vue';
import profilePage from '../templates/main/profile.vue';
import UsersList from '../templates/main/admin.vue';

Vue.use(VueRouter);

const routes = [
    { path: '/', name: 'Home', component: indexPage, alias: '/ciq' },
    { path: '/home', name: 'Home1', component: indexPage, alias: '/ciq/home' },
    { path: '/search', name: 'Search', component: searchPage, alias: '/ciq/search' },
    { path: '/profile', name: 'Profile', component: profilePage, alias: '/ciq/profile' },
    { path: '/showProfile', name: 'ShowProfile', component: showProfilePage, alias: '/ciq/showProfile' }
];



var router = new VueRouter ({
    routes: routes,
    //mode: 'history'
    mode: 'history',
    linkActiveClass: 'active'
});

export default router;
