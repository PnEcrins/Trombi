<template>
    <div>
        <div id="calendar"></div>
    </div>
</template>

<script>
// import FullCalendar from '@fullcalendar/vue3'
import { Calendar } from '@fullcalendar/core';

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
            console.log("USER", this.user.mail);
            let calendarEl = document.getElementById('calendar');
            this.calendar = new Calendar(calendarEl, {
                    plugins: [ dayGridPlugin, timeGridPlugin, interactionPlugin, FullCalendarICalendar, listPlugin ],
                    initialView: 'dayGridWeek',
                    events : {
                        url: `${this.$config.API_ENDPOINT}/caldav/${this.user.mail}`,
                    },
                    height: 600,
                    editable: true,
                    selectable: true,
                    headerToolbar: {
                        left: 'dayGridMonth,dayGridWeek,timeGridDay,listWeek',
                        center: 'title',
                        right: 'prev,next'
                    },
                    datesSet : this.dateChange,
                });
                this.calendar.render();
        }
    }

}
</script>

<style>

</style>