<template>
    <div>
        <div id="calendar"></div>
    </div>
</template>

<script>
// import FullCalendar from '@fullcalendar/vue3'
import { Calendar } from '@fullcalendar/core';
import frLocale from '@fullcalendar/core/locales/fr';

import tippy from 'tippy.js';
import 'tippy.js/dist/tippy.css';

import FullCalendarICalendar from '@fullcalendar/icalendar'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';



export default {
    name: "user-calendar",
    props : {
        user: Object,
    },
    watch: {
        user: function() {
            this.setUpCalendar();
        }

    },
    data() {
        return {
            calendar : null,
            nextButton: null,
            previousButton: null
        }
    },
    mounted() {
        this.setUpCalendar(this.user);
    },
    methods: {
        setUpCalendar() {
            let calendarEl = document.getElementById('calendar');
            this.calendar = new Calendar(calendarEl, {
                    locale: frLocale,
                    plugins: [ dayGridPlugin, timeGridPlugin, interactionPlugin, FullCalendarICalendar, listPlugin ],
                    initialView: 'timeGridWeek',
                    events : {
                        url: `${this.$config.API_ENDPOINT}/caldav/${this.user.mail}`,
                    },
                    // aspectRatio: 1,
                    slotMinTime: "06:00:00",
                    slotMaxTime: "20:00:00",
                    height: 600,
                    editable: true,
                    selectable: true,
                    headerToolbar: {
                        left: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek',
                        center: 'title',
                        right: 'prev,next'
                    },
                    datesSet : this.dateChange,
                    eventMouseEnter: this.handleMouseEnter,
                    eventDidMount: this.handlEventDidMount
                });
                this.calendar.render();
        },
        handleMouseEnter(info) {
            console.log(info.event);
            console.log(info.event.extendedProps);

        },
        handlEventDidMount(info) {
            const content = `
                <b> ${info.event.title} </b> <br/>
                <p>
                    <b> Organisateur </b> ${info.event.extendedProps.organizer} </br>
                     <b> Début </b> : ${info.event.extendedProps.begin_str}  </br>
                    <b> Fin </b> : ${info.event.extendedProps.end_str} </br>
                    <b> Lieu </b>: ${info.event.extendedProps.location}
                </p>
                <b> Participants </b>: ${info.event.extendedProps.attendees}
            `

            console.log(info.event);
            tippy(info.el, {
                content: content,
                allowHTML: true
            });
        }
    }

}
</script>

<style>

</style>