#!/usr/bin/yarn dev
import { createQueue, Job } from 'kue';

const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];
const queue = createQueue();

/**
 * Send push notification to user.
 * @param {string} phoneNumber
 * @param {string} message
 * @param {job} job
 * @param {*} done
 */
const sendNotification = (phoneNumber, message, job, done) => {
  let tot = 2, pnd = 2;
  let sendInterval = setInterval(() => {
    if (tot - pnd <= tot / 2) {
      job.progress(tot - pnd, tot);
    }
    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return;
    }
    if (tot === pnd) {
      console.log(
        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`,
      );
    }
    --pnd || done();
    pnd || clearInterval(sendInterval);
  }, 1000);
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});