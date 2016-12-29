<?php

namespace Tuto\TestBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;

<<<<<<< HEAD
class DefaultController extends Controller {

    public function testAction() {
        $film = $this->getDoctrine()
                ->getRepository('TutoTestBundle:films')
                ->findall();

        return $this->render('TutoTestBundle:Default:filmview.html.twig', array(
                    'film' => $film));
    }

    public function secondAction() {

        $director = $this->getDoctrine()
                ->getRepository('TutoTestBundle:Directors')
                ->findall();

        return $this->render('TutoTestBundle:Default:directorview.html.twig', array(
                    'director' => $director));
    }

    public function thirdAction() {

        $writer = $this->getDoctrine()
                ->getRepository('TutoTestBundle:writers')
                ->findall();

        return $this->render('TutoTestBundle:Default:writerview.html.twig', array(
                    'writer' => $writer));
    }

    public function indexAction() {


        return $this->render('TutoTestBundle:Default:index.html.twig');
    }

=======
class DefaultController extends Controller
{
    public function indexAction()
    {
        return $this->render('TutoTestBundle:Default:firstview.html.twig');
    }

    public function listeAction()
    {
        $film = $this->getDoctrine()
            ->getRepository('TutoTestBundle:Films')
        ->find(1);

        if($film) {
            return $this->render('TutoTestBundle:Default:index.html.twig', array(
                'film' => $film->getTitle(), 'year' => $film-> getYear(), 'bechdel' => $film-> getBechdel(),
            ));
        } else {
            return $this->render('TutoTestBundle:Default:index.html.twig',array(
                'film' => '',
                'year' => '',
                'bechdel' => '',

            ));
        }

    }



>>>>>>> upstream/dev
}
